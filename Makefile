style = src/_includes/styles/main.css
style_source = src/_styles/main.scss

serve: $(style)
	cd src && bundle exec jekyll serve --livereload --drafts --future --port 5000 --livereload_port 35729 "$@"

build: $(style)
	cd src && bundle exec jekyll build

css: $(style)

$(style): $(style_source)
	postcss "$<" -o "$@"
