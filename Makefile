JEKYLL_ENV = development

serve:
	JEKYLL_ENV=$(JEKYLL_ENV) bundle exec jekyll serve --livereload --drafts --future --port 5000 --livereload_port 35729 "$@"

build:
	JEKYLL_ENV=$(JEKYLL_ENV) bundle exec jekyll build

clean:
	JEKYLL_ENV=$(JEKYLL_ENV) bundle exec jekyll clean
