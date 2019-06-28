TAG="\n\n\033[0;32m\#\#\# "
END=" \#\#\# \033[0m\n"

HOST=localhost
PORT=9090
PYTHONPATH=nommo
DJANGO_SETTINGS=nommo.settings

# django-command = django-admin $(1) $(HOST):$(PORT) --settings $(DJANGO_SETTINGS) --pythonpath $(PYTHONPATH)
django-command = django-admin $(1) $(2) --settings $(DJANGO_SETTINGS) --pythonpath $(PYTHONPATH)

runserver:
	@echo $(TAG)Running Server $(END)
	$(call django-command, runserver, $(HOST):$(PORT))

shell:
	@echo $(TAG)Running Shell $(END)
	$(call django-command, shell)

migrate:
	@echo $(TAG)Migrating Database$(END)
	$(call django-command, migrate)

makemigrations:
	@echo $(TAG)Creating Migrations$(END)
	$(call django-command, makemigrations)

createsuperuser:
	@echo $(TAG)Create Superuser$(END)
	$(call django-command, createsuperuser)

load_initial_data:
	@echo $(TAG)Load initial data$(END)
	DJANGO_SETTINGS_MODULE=$(DJANGO_SETTINGS) PYTHONPATH=$(PYTHONPATH) python import_sample_data.py

notebook:
	PYTHONPATH=$(realpath sample_project) jupyter notebook --ip=127.0.0.1
