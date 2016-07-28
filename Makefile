run:
	dev_appserver.py --allow_skipped_files=true .

test:
	@curl \
	  -H 'content-type:application/json' \
	  -d '{"person": {"name": "Danny"}}' \
	  http://localhost:8080/_api/products.say_hello
