 curl \
  -H 'content-type:application/json' \
  -d '{"person": {"name": "Danny"}}' \
  http://localhost:8080/_api/products.say_hello
