# 📚 2026.04.22 Django 수업 정리

## Django Authentication 기능 구현

## 📌 프로젝트 개요

Django의 기본 인증 시스템을 활용하여 회원가입, 로그인, 로그아웃, 회원정보 수정, 비밀번호 변경 기능을 구현한 프로젝트입니다.

---

## 🛠 기술 스택

* Python 3.11
* Django 5.x
* SQLite3

---

## 📁 프로젝트 구조

```
config/
accounts/
articles/
templates/
static/
```

---

## 🔑 주요 기능

### 1. 회원가입 (Signup)

* `UserCreationForm`을 상속한 `CustomUserCreationForm` 사용
* 사용자 계정 생성

```python
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
```

---

### 2. 로그인 / 로그아웃

* Django 기본 인증 기능 사용
* 세션 기반 인증 처리

---

### 3. 회원 탈퇴 (Delete)

* 로그인된 사용자 계정 삭제

```python
@login_required
def delete(request):
    request.user.delete()
    return redirect('articles:index')
```

---

### 4. 회원정보 수정 (Update)

* `UserChangeForm`을 상속한 `CustomUserChangeForm` 사용
* 현재 로그인된 사용자 정보 수정

```python
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']
```

```python
@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
```

---

### 5. 비밀번호 변경 (Password Change)

* `PasswordChangeForm` 사용
* 로그인 상태에서 비밀번호 변경 가능

```python
@login_required
def password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
```

✔ `update_session_auth_hash` 사용 이유
→ 비밀번호 변경 후 자동 로그아웃 방지

---

## ⚠️ 트러블 슈팅

### 1. CustomUserChangeForm import 오류

* 원인: forms.py에 클래스 미정의
* 해결: 직접 클래스 생성

---

### 2. NoReverseMatch 오류

* 원인: 잘못된 URL (`articles:update` 사용)
* 해결: `accounts:update`로 수정

---

### 3. SetPasswordForm 오류

```
missing 1 required positional argument: 'user'
```

* 원인: form 생성 시 user 미전달
* 해결:

```python
PasswordChangeForm(request.user)
```

---

### 4. /accounts/ 404 오류

* 원인: 기본 경로 미설정
* 해결: redirect 또는 index view 추가

---

## 💡 느낀 점

* Django의 인증 시스템은 강력하지만, form과 view 연결 구조를 이해하는 것이 중요하다.
* 특히 `instance=request.user`와 같은 개념이 핵심이다.
* URL 네이밍과 template 연결이 매우 중요하다는 것을 체감했다.

---

## 🚀 실행 방법

```bash
python -m venv venv
source venv/Scripts/activate   # Windows

pip install django

python manage.py migrate
python manage.py runserver
```

---

## 📎 참고

* Django 공식 문서
* Django Authentication System
