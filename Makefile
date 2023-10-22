up_api:
	uvicorn api.main:app --reload
up_client:
	cd client && python -m http.server 8080