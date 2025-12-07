# .PHONY tells make that these are commands, not actual files
.PHONY: run-coverage run-clean-coverage open-report help

# Default target: Run coverage when you just type "make"
.DEFAULT_GOAL := run-coverage

# 1. Run the full coverage suite
run-coverage:
	@echo "🚀 Running tests with coverage..."
	python -m pytest
	@echo "✅ Done."

# 2. Run coverage and generate the HTML report
run-coverage-html:
	@echo "🚀 Generating HTML report..."
	python -m pytest --cov-report html
	@echo "📄 Report generated at htmlcov/index.html"

# 3. Clean up all artifacts
run-clean-coverage:
	@echo "🧹 Cleaning up..."
	rm -rf .coverage
	rm -rf coverage.xml
	rm -rf htmlcov
	rm -rf .pytest_cache
	# Optional: Remove python cache files
	find . -type d -name "__pycache__" -exec rm -rf {} +
	@echo "✨ Cleaned."

# 4. Helper to open the report (Mac/Linux specific)
open-report:
	@# Uses 'open' on Mac or 'xdg-open' on Linux
	@(open htmlcov/index.html || xdg-open htmlcov/index.html) 2>/dev/null || echo "Open htmlcov/index.html manually."

# 5. Create a new day scaffold
# Usage: make init day=5
init:
	@if [ -z "$(day)" ]; then \
		echo "❌ Error: Missing day argument. Usage: make init day=5"; \
		exit 1; \
	fi
	@echo "📅 Initializing Day $(day)..."
	python scripts/init_day.py $(day)

# 6. Help menu
help:
	@echo "Available commands:"
	@echo "  make run-coverage        : Run tests with terminal coverage report"
	@echo "  make run-coverage-html   : Run tests and create HTML report"
	@echo "  make run-clean-coverage  : Delete all coverage artifacts"
	@echo "  make open-report         : Open the HTML report in your browser"
	@echo "  make init day=N          : Initialize boilerplate for Day N (e.g., make init day=5)"
