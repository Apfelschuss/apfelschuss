from django.utils import translation


# user_language = 'en'
# translation.activate(user_language)
# request.session[translation.LANGUAGE_SESSION_KEY] = user_language

if translation.LANGUAGE_SESSION_KEY in request.session:
    del request.session[translation.LANGUAGE_SESSION_KEY]
