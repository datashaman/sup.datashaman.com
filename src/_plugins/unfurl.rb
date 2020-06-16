require 'uri'
require 'oembed'

OEmbed::Providers::register_all

Jekyll::Hooks.register :posts, :pre_render do |post|
    URI.extract(post.content) do |url|
        if url.start_with?('http') then
            begin
                resource = OEmbed::Providers.get(url)
                post.content += "\n" + resource.html
            rescue OEmbed::NotFound
            end
        end
    end
end
