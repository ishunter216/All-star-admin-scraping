from app import app, models, db
from flask import render_template, request, redirect, flash
from .forms import InductionForm, ApprovalForm
from .models import Order, Image
from datetime import datetime
from flask_security import current_user, login_required, logout_user

from binascii import a2b_base64
import boto3
from uuid import uuid4
import json

S3_BUCKET = app.config['S3_BUCKET']

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/induction', methods=['GET', 'POST'])
def induction():
	return redirect("approval")
	form = InductionForm()

	if request.method == 'POST':
		if form.validate():
			if form.correct_to_invoice.data == 'y':
				correct = True
			else:
				correct = False
				
			if form.replacement_available.data == 'y':
				replacement = True
			else:
				replacement = False

			if form.light_noted.data == 'y':
				noted = True
			else:
				noted = False

			if correct:
				r = models.Order(invoice_num=form.invoice_num.data, side=form.side.data, light_type=form.light_type.data, correct_to_invoice=correct,
					induction_employee_code=form.induction_employee_code.data, light_noted=noted, induction_date=datetime.now(), status='Pending',
					light_type_comments=form.light_type_comments.data)
			else:
				r = models.Order(invoice_num=form.invoice_num.data, side=form.side.data, light_type=form.light_type.data, correct_to_invoice=correct,
					induction_employee_code=form.induction_employee_code.data, induction_date=datetime.now(), status='Rejected',
					replacement_available=replacement, replacement_comments=form.replacement_comments.data,
					light_type_comments=form.light_type_comments.data)

			db.session.add(r)
			db.session.commit()

			#return render_template('thanks.html')
			flash('Record saved.')
			return redirect("induction")
		else:
			print(form.errors)

	return render_template('induction.html', form=form)

@app.route('/deletePic',methods=['POST'])
def deletePic():
	return (200,"")


@app.route('/approval', methods=['GET', 'POST'])
def approval():
	form = ApprovalForm()

	if request.method == 'POST':
		if form.validate():
			#Add any images to S3_Bucket
			s3 = boto3.resource('s3')
			"""
			if image_URI_list[len(image_URI_list)-1] == None or image_URI_list[len(image_URI_list)-1] == '':
				image_URI_list = image_URI_list[:-1]
				print
				print
				print("FOUND BLANK IMAGE")
				print("length of list is..")
				print(len(image_URI_list))
			"""
			s3_image_list = []
			files = request.files.getlist('files[]')
			if files:
				for f in files:
					if (f.content_type == 'image/png'):
						base64_URI = f.stream
						s3_filename = uuid4().hex + '.png' #Generate random filename
						s3.Bucket(S3_BUCKET).put_object(Key=s3_filename, Body=base64_URI,ContentType='image/png',ACL='public-read')
						i = models.Image(file_name=s3_filename,s3_bucket=S3_BUCKET,approval_date=datetime.now())
						s3_image_list.append(i)

			"""
			if form.approval_type.data == 'Recon':

				r = Order.query.filter_by(invoice_num=form.invoice_num.data).first()

				for s3_image in s3_image_list:
					r.images.append(s3_image)

				r.approval_employee_code = form.approval_employee_code.data
				r.tracking_number = form.tracking_number.data

				if form.have_repair.data == 'y':
					r.have_repair = True
					r.repair_comments = form.repair_comments.data
				else:
					r.have_repair = False
				
				if form.stickered_engraved.data == 'y':
					r.stickered_engraved = True
				else:
					r.stickered_engraved = False

				r.light_approved = form.light_approved.data
				if form.light_approved.data != 'Yes':
					r.approval_comments = form.approval_comments.data

				r.approval_type = 'Recon'
				r.notes = form.notes.data
				r.approval_date = datetime.now()
				r.status = 'Approved'

			else:
			"""
			print("SWAP: " + str(form.swap_out.data))

			if form.light_approved.data != 'Yes':
				comm = form.approval_comments.data
			else:
				comm = ''


			r = models.Order(invoice_num=form.invoice_num.data,
				tracking_number=form.tracking_number.data,
				approval_employee_code=form.approval_employee_code.data,
				light_approved=form.light_approved.data, 
				notes=form.notes.data, 
				approval_comments=comm, 
				approval_type=form.approval_type.data, 
				light_type=form.light_type.data,
				interchange=form.interchange.data,
				approval_date=datetime.now(),
				tested_bare=form.tested_bare.data,
				repair_comments = form.repair_comments.data,
				have_repair=form.have_repair.data,
				swap_out=form.swap_out.data,
				bake_wash=form.bake_wash.data,
				light_noted=form.light_noted.data,
				status='Approved')


			for s3_image in s3_image_list:
				r.images.append(s3_image)

			db.session.add(r)

			db.session.commit()

			flash('Record saved.')
			return redirect("approval")
		else:
			return json.dumps(form.errors)

	return render_template('approval.html', form=form)


@app.route("/logout", methods=['GET', 'POST'])
def logout():
    """Logout the current user."""
    logout_user()
    return render_template('admin/loggedout.html') 