import os
import uuid
from werkzeug.utils import secure_filename
from flask import Blueprint, render_template, current_app, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.forms import PhotoForm, LoginForm
from app.models import Photo, User

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/gallery')
def gallery():
    photos = Photo.query.order_by(Photo.created_at.desc()).all()
    return render_template('gallery.html', photos=photos)

@main.route('/admin/upload', methods=['GET', 'POST'])
@login_required
def upload_photo():
    form = PhotoForm()
    if form.validate_on_submit():
        # Uzimamo otpremljeni fajl
        f = form.image.data
        filename = secure_filename(f.filename)
        
        # Pravimo jedinstven naziv fajla da sprečimo preklapanje
        unique_filename = str(uuid.uuid4()) + "_" + filename
        
        # Definišemo putanju gde se slika fizički čuva
        upload_path = os.path.join(current_app.root_path, 'static', 'uploads', unique_filename)
        f.save(upload_path)
        
        # Upisujemo podatke u bazu podataka preko našeg Photo modela
        photo = Photo(
            title=form.title.data,
            description=form.description.data,
            category=form.category.data,
            image_file=unique_filename
        )
        db.session.add(photo)
        db.session.commit()
        
        flash('Fotografija je uspešno otpremljena!', 'success')
        return redirect(url_for('main.gallery'))
        
    return render_template('admin/upload.html', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
        
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Uspešno si se prijavio!', 'success')
            return redirect(url_for('main.upload_photo'))
        else:
            flash('Neuspešna prijava. Proveri email i lozinku.', 'danger')
            
    return render_template('admin/login.html', form=form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Uspešno si se odjavio.', 'info')
    return redirect(url_for('main.index'))