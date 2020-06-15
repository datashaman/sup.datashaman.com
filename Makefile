serve:
	bundle exec jekyll serve --livereload --drafts --future --port 5000 --livereload_port 35729 "$@"

build-css:
	tailwindcss build _site/css/main.css -o _site/css/main.css
