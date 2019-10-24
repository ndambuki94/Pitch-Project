from flask import render_template, request, redirect, url_for, abort
from . import main
from flask_login import login_required, current_user
from ..models import User, Category, Pitches, Comments
from .forms import UpdateProfile , CommentForm,PitchForm
from .. import db, photos



