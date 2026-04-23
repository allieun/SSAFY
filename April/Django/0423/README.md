# 📚 2026.04.22 Django 수업 정리

## 📌 학습 주제
- Custom User Model 기반 인증 기능 구현
- 로그인 / 로그아웃 / 회원탈퇴 기능 확장

---

## 🔑 오늘 학습 내용

### 1. 로그인 / 로그아웃 구현
- `AuthenticationForm` 사용
- `auth_login`, `auth_logout` 활용
- 로그인 상태 유지 (세션)

---

### 2. 회원탈퇴 기능
- 로그인된 사용자만 탈퇴 가능
- `request.user.delete()`로 계정 삭제
- 탈퇴 후 자동 로그아웃 처리

```python
def delete(request):
    if request.method == 'POST':
        request.user.delete()
        auth_logout(request)
    return redirect('accounts:index')
```
### 3. 전체 유저 목록 조회
- get_user_model() 사용
- 커스텀 User 모델 대응
```python
User = get_user_model()
users = User.objects.all()
```
### 4. 템플릿에서 로그인 상태 분기
- `user.is_authenticated` 활용
```Django html
hello,
{% if user.is_authenticated %}
  {{ user.username }}
{% endif %}
```

### 💡 핵심 포인트
- User 모델은 get_user_model()로 접근
- 로그인/로그아웃은 Django auth 사용
- 로그아웃 / 회원탈퇴는 POST 방식
- UI는 로그인 상태에 따라 분기
### ⚠️ 트러블 슈팅
#### ❗ User.object 오류
```python
User.object.all()
```
➡️ objects로 수정 필요

#### ❗ 회원탈퇴 버튼 안 보임
- value 오타 (valeu) 수정
- 로그인 조건문 위치 확인
### ✅ 느낀 점
- Django 인증 시스템 구조를 이해하면 구현이 빠르다
- is_authenticated를 활용한 템플릿 분기가 중요하다