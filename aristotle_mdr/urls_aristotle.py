import autocomplete_light
autocomplete_light.autodiscover()

from django.conf.urls import patterns, url

import aristotle_mdr.views as views
import aristotle_mdr.forms as forms
from django.views.generic import TemplateView

from haystack.query import SearchQuerySet
from haystack.views import search_view_factory

sqs = SearchQuerySet()

"""
    url(r'^property/(?P<iid>\d+)?/?$', views.items.property, name='property'),
    url(r'^valuedomain/(?P<iid>\d+)?/?$', views.items.valuedomain, name='valueDomain'),
    url(r'^conceptualdomain/(?P<iid>\d+)?/?$', views.items.conceptualdomain, name='conceptualDomain'),
    url(r'^dataelementconcept/(?P<iid>\d+)?/?$', views.items.dataelementconcept, name='dataElementConcept'),
    url(r'^dataelement/(?P<iid>\d+)?(?:-[a-z\-]*)?/?$', views.items.dataelement, name='dataElement'),
    url(r'^dataelementderivation/(?P<iid>\d+)?(?:-[a-z\-]*)?/?$', views.items.dataelementderivation, name='dataElementDerivation'),
    url(r'^datatype/(?P<iid>\d+)/?$', views.items.datatype, name='dataType'),
    url(r'^unitofmeasure/(?P<iid>\d+)/?$', views.items.unitofmeasure, name='unitOfMeasure'),
    url(r'^package/(?P<iid>\d+)/?$', views.items.package, name='package'),
    """

urlpatterns = patterns('aristotle_mdr.views',
    url(r'^/?$', TemplateView.as_view(template_name='aristotle_mdr/static/home.html'),name="home"),

    # all the below take on the same form:
    # url(r'^itemType/(?P<iid>\d+)?/?
    # Allowing for a blank ItemId (iid) allows aristotle to redirect to /about/itemtype instead of 404ing
    url(r'^valuedomain/(?P<iid>\d+)?/edit/values/(?P<value_type>permissible|supplementary)/?$', views.valuedomain_value_edit, name='valueDomain_edit_values'),

    url(r'^glossary/?$', views.glossary, name='glossary'),

    url(r'^workgroup/(?P<iid>\d+)/?$', views.workgroups.workgroup, name='workgroup'),
    url(r'^workgroup/(?P<iid>\d+)/members/?$', views.workgroups.members, name='workgroupMembers'),
    url(r'^workgroup/(?P<iid>\d+)/items/?$', views.workgroups.items, name='workgroupItems'),
    url(r'^workgroup/addMembers/(?P<iid>\d+)$', views.workgroups.add_members, name='addWorkgroupMembers'),
    url(r'^remove/WorkgroupRole/(?P<iid>\d+)/(?P<role>[A-Za-z\-]+)/(?P<userid>\d+)/?$', views.workgroups.remove_role, name='removeWorkgroupRole'),

    url(r'^discussions/?$', views.discussions.all, name='discussions'),
    url(r'^discussions/new/?$', views.discussions.new, name='discussionsNew'),
    url(r'^discussions/workgroup/(?P<wgid>\d+)/?$', views.discussions.workgroup, name='discussionsWorkgroup'),
    url(r'^discussions/post/(?P<pid>\d+)/?$', views.discussions.post, name='discussionsPost'),
    url(r'^discussions/post/(?P<pid>\d+)/newcomment/?$', views.discussions.new_comment, name='discussionsPostNewComment'),
    url(r'^discussions/delete/comment/(?P<cid>\d+)/?$', views.discussions.delete_comment, name='discussionsDeleteComment'),
    url(r'^discussions/delete/post/(?P<pid>\d+)/?$', views.discussions.delete_post, name='discussionsDeletePost'),
    url(r'^discussions/edit/comment/(?P<cid>\d+)/?$', views.discussions.edit_comment, name='discussionsEditComment'),
    url(r'^discussions/edit/post/(?P<pid>\d+)/?$', views.discussions.edit_post, name='discussionsEditPost'),
    url(r'^discussions/post/(?P<pid>\d+)/toggle/?$', views.discussions.toggle_post, name='discussionsPostToggle'),

    #url(r'^item/(?P<iid>\d+)/?$', views.items.concept, name='item'),
    url(r'^item/(?P<iid>\d+)(?:\/(?P<model_slug>\w+)\/(?P<name_slug>.+))?/?$', views.concept, name='item'),
    url(r'^item/(?P<iid>\d+)/edit/?$', views.edit_item, name='edit_item'),
    url(r'^item/(?P<iid>\d+)/packages/?$', views.itemPackages, name='itemPackages'),
    url(r'^item/(?P<iid>\d+)/registrationHistory/?$', views.registrationHistory, name='registrationHistory'),
    url(r'^item/(?P<iid>\d+)(?:\/.*)?$', views.concept, name='item'), # Catch every other 'item' URL and throw it for a redirect

    #url(r'^create/?$', views.item, name='item'),
    url(r'^create/?$', views.create_list, name='createList'),
    url(r'^create/(aristotle_mdr/)?dataelementconcept$', views.wizards.DataElementConceptWizard.as_view(), name='createDataElementConcept'),
    url(r'^create/(aristotle_mdr/)?dataelement$', views.wizards.DataElementWizard.as_view(), name='createDataElement'),
    url(r'^create/(?P<app_label>.+)/(?P<model_name>.+)/?$', views.wizards.create_item, name='createItem'),
    url(r'^create/(?P<model_name>.+)/?$', views.wizards.create_item, name='createItem'),

    url(r'^download/(?P<downloadType>[a-zA-Z0-9\-\.]+)/(?P<iid>\d+)/?$', views.download, name='download'),

    url(r'^action/supersede/(?P<iid>\d+)$', views.supersede, name='supersede'),
    url(r'^action/deprecate/(?P<iid>\d+)$', views.deprecate, name='deprecate'),
    url(r'^action/bulkaction/?$', views.bulk_action, name='bulk_action'),
    url(r'^action/r2r/(?P<iid>\d+)?$', views.mark_ready_to_review, name='mark_ready_to_review'),

    url(r'^changestatus/(?P<iid>\d+)$', views.changeStatus, name='changeStatus'),
    #url(r'^remove/WorkgroupUser/(?P<iid>\d+)/(?P<userid>\d+)$', views.removeWorkgroupUser, name='removeWorkgroupUser'),

    url(r'^account/home/?$', views.user_pages.home, name='userHome'),
    url(r'^account/userAdminTools/?$', views.user_pages.admin_tools, name='userAdminTools'),
    url(r'^account/edit/?$', views.user_pages.edit, name='userEdit'),
    url(r'^account/favourites/?$', views.user_pages.favourites, name='userFavourites'),
    url(r'^account/workgroups/?$', views.user_pages.workgroups, name='userWorkgroups'),
    url(r'^account/notifications(?:/folder/(?P<folder>all))?/?$', views.user_pages.inbox, name='userInbox'),

    url(r'^account/registrartools/?$', views.user_pages.registrar_tools, name='userRegistrarTools'),
    url(r'^account/registrartools/readyforreview/?$', views.user_pages.review_list, name='userReadyForReview'),

    url(r'^registrationauthority/(?P<iid>\d+)?/?$', views.registrationauthority, name='registrationAuthority'),
    url(r'^registrationauthorities/?$', views.allRegistrationAuthorities, name='allRegistrationAuthorities'),
    url(r'^account/toggleFavourite/(?P<iid>\d+)/?$', views.toggleFavourite, name='toggleFavourite'),

    url(r'^browse(?:/(?P<oc_id>\d+)(?:-[a-z\-]*)?(?:/(?P<dec_id>\d+)(?:-[a-z\-]*)?)?)?/?$', views.browse, name='browse'),

    url(r'^about/aristotle/?$', TemplateView.as_view(template_name='aristotle_mdr/static/aristotle_mdr.html'), name="aboutMain"),
    url(r'^about/all_items/?$', views.about_all_items, name='about_all_items'),
    url(r'^about/(?P<template>.+)/?$', views.DynamicTemplateView.as_view(), name="about"),
    url(r'^help/(?P<template>.+)/?$', views.HelpTemplateView.as_view(), name="help"),
    url(r'^help/?$', TemplateView.as_view(template_name='aristotle_mdr/static/help/help.html'), name="helpMain"),


    url(r'^about/?$', TemplateView.as_view(template_name='site/about.html'), name="aboutThisSite"),
    url(r'^privacy/?$', TemplateView.as_view(template_name='site/privacy.html'), name="privacy"),
    url(r'^copyright/?$', TemplateView.as_view(template_name='site/copyright.html'), name="copyright"),
    url(r'^disclaimer/?$', TemplateView.as_view(template_name='site/disclaimer.html'), name="disclaimer"),
    url(r'^accessibility/?$', TemplateView.as_view(template_name='site/accessibility.html'), name="accessibility"),
    url(r'^contact/?$', TemplateView.as_view(template_name='site/contact.html'), name="contact"),

    url(r'^search/?', search_view_factory(
     view_class=views.PermissionSearchView,
     template='search/search.html',
     searchqueryset=sqs,
     form_class=forms.search.PermissionSearchForm
     ), name='search'),
)

