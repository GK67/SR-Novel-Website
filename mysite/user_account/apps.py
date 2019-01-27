from django.apps import AppConfig


class UserAccountConfig(AppConfig):
    name = 'user_account'

    def ready(self):
    	import user_account.signals

