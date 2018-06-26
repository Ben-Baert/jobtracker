from django.contrib.auth.models import User
from django.db import models


class DiscussionGroup(models.Model):
    name = models.CharField(max_length=50)


class DiscussionGroupMembership(models.Model):
    discussion_group = models.ForeignKey(DiscussionGroup, related_name='members')
    user = models.ForeignKey(User, related_name='memberships')


class Company(models.Model):
    name = models.CharField(max_length=50)


class Country(models.Model):
    name = models.CharField(max_length=50)


class Location(models.Model):
    country = models.ForeignKey(Country, related_name='locations')
    name = models.CharField(max_length=5)


class Job(models.Model):
    discussion_group = models.ForeignKey(DiscussionGroup, related_name='jobs')
    company = models.ForeignKey(Company, related_name='jobs')
    location = models.ForeignKey(Location, related_name='jobs')
    position = models.CharField(max_length=200)
    description = models.TextField(null=True)

    applied = models.BooleanField(default=False)
    heard_back = models.BooleanField(default=False)
    got_interview = models.BooleanField(default=False)
    interview_dt = models.DateTimeField(null=True)
    got_job_offer = models.BooleanField(default=False)
    got_rejected = models.BooleanField(default=False)


class JobCriterion(models.Model):
    name = models.CharField(max_length=50)
    importance = models.IntegerField(default=5)


class JobRating(models.Model):
    user = models.ForeignKey(User, related_name='job_ratings')
    job = models.ForeignKey(Job, related_name='ratings')
    criterion = models.ForeignKey(JobCriterion, related_name='ratings')
    rating = models.IntegerField()
    comment = models.TextField(null=True)


class JobComment(models.Model):
    user = models.ForeignKey(User, related_name='comments')
    job = models.ForeignKey(Job, related_name='comments')
    parent = models.ForeignKey('self', related_name='children')
    body = models.TextField()


class JobRejection(models.Model):
    user = models.ForeignKey(User, related_name='job_rejections')
    job = models.ForeignKey(Job, related_name='rejections')
    reason = models.TextField(null=True)
