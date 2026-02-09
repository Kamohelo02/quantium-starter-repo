# run_tests.ps1

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Run tests
python -m pytest test_app.py -v

# Capture exit code
$TEST_EXIT_CODE = $LASTEXITCODE

# Deactivate
deactivate

# Exit with test's exit code
exit $TEST_EXIT_CODE
