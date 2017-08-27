
from misago.threads.api.postingendpoint import PostingMiddleware

from misago.conf import settings


TRUSTED_DOMAINS = getattr(settings, "MISAGO_TRUSTED_DOMAINS", [])


class ModerateIfContainsLinkMiddleware(PostingMiddleware):

    def save(self, serializer):

        for domain in self.post.parsing_result.get("outgoing_links", []):
            second_tld = domain.partition("/")[0].rsplit(".", 2)[-2:]
            second_tld = '.'.join(second_tld)
            if second_tld not in TRUSTED_DOMAINS:
                self.post.is_unapproved = True
                break

        if self.post.is_unapproved:
            self.post.update_fields.append('is_unapproved')