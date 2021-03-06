import functools
from typing import Callable
from flask import session, flash, redirect, url_for, current_app


def requires_login(f: Callable) -> Callable:
    @functools.wraps(f)
    def decorated_func(*args, **kwargs):
        if not session.get("email"):
            flash("You need to be signed in for this page", "danger")
            return redirect(url_for("users.login_user"))
        return f(*args, **kwargs)

    return decorated_func


def requires_admin(f: Callable) -> Callable:
    @functools.wraps(f)
    def decorated_func(*args, **kwargs):
        if session.get("email") != current_app.config.get("ADMIN", ""):
            flash("Only admin is granted access to this page", "danger")
            return redirect(url_for("user.login_user"))
        return f(*args, **kwargs)

    return decorated_func

