# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.core.mail import send_mass_mail
# from django.template.loader import render_to_string
# from django.contrib.auth import get_user_model
# from .models import Blog
#
# @receiver(post_save,sender=Blog)
# def send_notification(sender, instance, **kwargs):
#     subject = 'New Blog Post Notification'
#     message = render_to_string('blog/notification.html', {'blog':instance})
#     users_to_notify = get_user_model().objects.all()
#
#     recipient_list = [user.email for user in users_to_notify]
#
#     if recipient_list:
#         email_message = (subject, message, 'olakay739@gmail.com', recipient_list)
#         send_mass_mail((email_message,), fail_silently=False)