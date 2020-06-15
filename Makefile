css = src/css/main.css
css_source = src/_sass/main.scss

serve: $(css)
	bundle exec jekyll serve --livereload --drafts --future --port 5000 --livereload_port 35729 --source src "$@"

build: $(css)
	bundle exec jekyll build --source src

css: $(css)

$(css): $(css_source)
	postcss "$<" -o "$@"
