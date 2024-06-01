# Имя виртуального окружения
VENV = venv

# Файл с зависимостями
REQUIREMENTS = requirements.txt

# Команда для создания виртуального окружения
$(VENV)/bin/activate:
	python3 -m venv $(VENV)

# Команда для установки зависимостей
install: $(VENV)/bin/activate
	. $(VENV)/bin/activate && pip install -r $(REQUIREMENTS)

# Команда для подготовки окружения
prepare-env: install

.PHONY: prepare-env install
