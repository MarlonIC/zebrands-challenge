#!/bin/sh
exec gunicorn wsgi:app -b 0.0.0.0:80