# Makefile pour automatiser les tâches

# Variables
PYTHON = python3
STREAMLIT = streamlit
DB_FILE = path/to/your/database.db  # Remplace par le chemin de ton fichier .db

# Cible par défaut
.PHONY: all
all: clean load_data run_app

# Supprimer le fichier .db avant d'exécuter d'autres tâches
.PHONY: clean
clean:
	@echo "Suppression du fichier .db..."
	rm -f $(DB_FILE)

# Charger les données
.PHONY: load_data
load_data:
	$(PYTHON) load_data.py

# Lancer l'application Streamlit
.PHONY: run_app
run_app:
	$(STREAMLIT) run app.py