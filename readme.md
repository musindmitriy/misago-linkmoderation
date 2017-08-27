# Misago Link Moderation

Plugin that allows to turn unapproved posts, that contain outgoing links
(like a similar setting in [Disqus](https://disqus.com) comment system) for your [Misago](https://misago-project.org) forum.

Installation
------------

Put `misagolinkmoderation` directory under your python path,
then add following entry to your installation settings:

```python
MISAGO_POSTING_MIDDLEWARES = [
    # Always keep FloodProtectionMiddleware middleware first one
    'misago.threads.api.postingendpoint.floodprotection.FloodProtectionMiddleware',

    'misago.threads.api.postingendpoint.category.CategoryMiddleware',
    'misago.threads.api.postingendpoint.privatethread.PrivateThreadMiddleware',
    'misago.threads.api.postingendpoint.reply.ReplyMiddleware',
    'misago.threads.api.postingendpoint.moderationqueue.ModerationQueueMiddleware',

    'misagolinkmoderation.moderation.ModerateIfContainsLinkMiddleware',

    'misago.threads.api.postingendpoint.attachments.AttachmentsMiddleware',
    'misago.threads.api.postingendpoint.participants.ParticipantsMiddleware',
    'misago.threads.api.postingendpoint.pin.PinMiddleware',
    'misago.threads.api.postingendpoint.close.CloseMiddleware',
    'misago.threads.api.postingendpoint.hide.HideMiddleware',
    'misago.threads.api.postingendpoint.protect.ProtectMiddleware',
    'misago.threads.api.postingendpoint.recordedit.RecordEditMiddleware',
    'misago.threads.api.postingendpoint.updatestats.UpdateStatsMiddleware',
    'misago.threads.api.postingendpoint.mentions.MentionsMiddleware',
    'misago.threads.api.postingendpoint.subscribe.SubscribeMiddleware',
    'misago.threads.api.postingendpoint.syncprivatethreads.SyncPrivateThreadsMiddleware',

    # Always keep SaveChangesMiddleware middleware after all state-changing middlewares
    'misago.threads.api.postingendpoint.savechanges.SaveChangesMiddleware',

    # Those middlewares are last because they don't change app state
    'misago.threads.api.postingendpoint.emailnotification.EmailNotificationMiddleware',
]
```


Finally, you can set list of trusted domains (which your users allow to link without moderation):

```python
MISAGO_TRUSTED_DOMAINS = [  # And their subdomains
    'wikipedia.org',
]
```


Copyright and license
---------------------
 
> This program comes with ABSOLUTELY NO WARRANTY.  
> This is free software and you are welcome to redistribute it under the conditions described in the license.
>
> For the complete license, refer to [LICENSE.md](LICENSE.md)
