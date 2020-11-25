from flask import render_template, url_for, flash, redirect, request, Markup, abort, make_response
from website import application
from website.content import about_section
from website.utils import generate_tiers

@application.route("/")
def home():
    opening = about_section.opening_section
    qs = about_section.content_qs
    offers = about_section.content_offers
    final = about_section.content_final
    return render_template('base.html',
                           opening = opening,
                           qs=qs,
                           offers=offers,
                           final=final,
                           rules=False)


@application.route("/generate")
def generate_rules():
    rules = generate_tiers()
    state = rules[0]
    tiers = rules[1]
    opening = about_section.opening_section
    qs = about_section.content_qs
    offers = about_section.content_offers
    final = about_section.content_final
    return render_template('base.html',
                           opening=opening,
                           qs=qs,
                           offers=offers,
                           final=final,
                           rules=True,
                           state=state,
                           tiers=tiers
                           )

@application.route("/generate_rules")
def anch_redirect():
    return redirect(url_for('generate_rules', _anchor='generate_rules'))


@application.context_processor
def inject_template_scope():
    injections = dict()

    def cookies_check():
        value = request.cookies.get('cookie_consent')
        return value == 'true'
    injections.update(cookies_check=cookies_check)

    return injections

@application.route("/cookie_consent")
def consent():
    return render_template('consent.html')