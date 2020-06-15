css = src/css/main.css
css_source = src/_sass/main.scss

serve: $(css)
	cd src && bundle exec jekyll serve --livereload --drafts --future --port 5000 --livereload_port 35729 "$@"

build: $(css)
	cd src && bundle exec jekyll build

css: $(css)

$(css): $(css_source)
	postcss "$<" -o "$@"
