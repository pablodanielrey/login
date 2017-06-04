#!/bin/bash
curl -i -H "Content-Type: application/json" -X POST -d '{"username":"prueba", "password":"prueba"}' http://127.0.0.1:5000/login/api/v1.0/login
