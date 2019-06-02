from flask import g, render_template, session, request, flash, redirect, url_for
from src import app
from src.service import member_service
from src.model.account_form import SignupForm, SigninForm

m_service = member_service.Member_service()

@app.route('/signin/', methods=['GET', 'POST'])
def signin():
    if 'email' not in session and request.method == 'GET':
        return render_template('member/signin.html', account_form=g.account_form), 200

    form = SigninForm()
    if 'email' not in session and form.validate_on_submit():
        access_account_result = m_service.access_account(form)

        if access_account_result:
            # insert for session
            session['email'] = access_account_result[0]['email'] # unique index
            session['nickname'] = access_account_result[0]['nickname'] # user nickname

            flash(f'[Success] You are successfully Sign In for {form.email.data} account!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'[Failure] There is no account information about {form.email.data}, or a password mismatched', 'warning')
            return render_template('/member/signin.html', account_form=form), 200

    flash(f'[Warning] Invalid Information, try again please', 'warning')
    return render_template('member/signin.html', account_form=form), 200

@app.route('/signout/', methods=['GET'])
def signout():
    if 'email' in session:
        session.pop('email', None)
        flash(f'[Success] You are successfully sign out! Bye~', 'success')
        return redirect(url_for('home'))
    else:
        flash(f'[Warning] You must sign in this web site first', 'warning')
        return redirect(url_for('signin'))

@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('member/signup.html', account_form=g.account_form), 200

    form = SignupForm()
    if form.validate_on_submit():
        create_account_result = m_service.create_account(app.instance_path, form)

        ## 분기 : 등록 성공(1, home) / 파일 저장 실패(2) / duplicate key error(3) / db error(4)
        if create_account_result == 1:
            flash(f'[Success] 등록 성공 ({form.email.data})', 'success')
            return redirect(url_for('home'))
        elif create_account_result == 2:
            flash(f'[Warning] 파일 업로드 실패 ({form.email.data})', 'warning')
        elif create_account_result == 3:
            flash(f'[Warning] 이미 가입되어 있는 이메일입니다. ({form.email.data})', 'warning')
        else:
            flash(f'[Danger] 등록 실패. 관리자에게 문의하십시오. ({form.email.data})', 'danger')

    else:
        flash(f'[Failure] Invalid Information, try again please', 'warning')

    return render_template('member/signup.html', account_form=form), 200

@app.route('/delete_account/', methods=['GET', 'POST'])
def delete_account():
    if request.method == 'GET':
        pass
    else:
        pass