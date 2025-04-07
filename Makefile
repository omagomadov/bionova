.PHONY: clean all load run

PYTHON = python3
STREAMLIT = streamlit

all: clean load

clean:
	rm -rf chroma_db

load:
	$(PYTHON) load_data.py

run:
	$(STREAMLIT) run app.py