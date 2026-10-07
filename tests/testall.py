"""
Test suite for automation logging library
"""
import pytest
import os
from datetime import datetime
from pathlib import Path
import main

@pytest.fixture
def temp_log(tmp_path):
    """Create temporary log file for testing"""
    log_file = tmp_path / "test.log"
    main.conf.path = str(log_file)
    yield log_file
    # Cleanup
    if log_file.exists():
        log_file.unlink()

def test_printl_writes_to_file(temp_log):
    """Test that printl writes to log file"""
    main.printl("test message")
    content = temp_log.read_text()
    assert "test message" in content

def test_printl_appends_newline(temp_log):
    """Test that printl appends newline"""
    main.printl("line1")
    main.printl("line2")
    content = temp_log.read_text()
    lines = content.strip().split('\n')
    assert len(lines) == 2
    assert lines[0] == "line1"
    assert lines[1] == "line2"

def test_format_message(temp_log):
    """Test message formatting"""
    msg = main._format_message("INFO", "test")
    assert "INFO" in msg
    assert "test" in msg
    assert "[" in msg and "]" in msg

def test_fatal(temp_log):
    """Test fatal logging"""
    main.fatal("fatal error")
    content = temp_log.read_text()
    assert "FATAL" in content
    assert "fatal error" in content

def test_error(temp_log):
    """Test error logging"""
    main.error("error message")
    content = temp_log.read_text()
    assert "ERROR" in content
    assert "error message" in content

def test_warn(temp_log):
    """Test warning logging"""
    main.warn("warning message")
    content = temp_log.read_text()
    assert "WARN" in content
    assert "warning message" in content

def test_info(temp_log):
    """Test info logging"""
    main.info("info message")
    content = temp_log.read_text()
    assert "INFO" in content
    assert "info message" in content

def test_print_head(temp_log):
    """Test print_head"""
    main.print_head("test_script")
    content = temp_log.read_text()
    assert "TEAR  HERE" in content
    assert "This event is... test_script" in content
    assert "The timestamp for this event is..." in content

def test_print_foot(temp_log):
    """Test print_foot"""
    main.print_foot(0, "success")
    content = temp_log.read_text()
    assert "##### [REPORT] #####" in content
    assert "Exit code... 0" in content
    assert "Exit message... success" in content
    assert "Finished..." in content
    assert "##### [END REPORT] #####" in content

def test_multiple_entries(temp_log):
    """Test multiple log entries"""
    main.print_head("test")
    main.info("first")
    main.error("second")
    main.print_foot(1, "failed")
    
    content = temp_log.read_text()
    assert content.count("TEAR  HERE") >= 1
    assert "first" in content
    assert "second" in content
    assert "REPORT" in content
