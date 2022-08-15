# drf-auth

> To run the app make sure that you have Docker desktop app then run the following:
>
> $ docker-compose run web python manage.py migrate
>
> then create a super user
>
> $ docker-compose run web python manage.py createsuperuser
>
> $ docker-compose up
>
>
> then you can navigate to one of the following routes:
>> /admin/
>
>> /api/v1/articles/
>
>> /api/token/
>
>> /api/token/refresh/


Testing:
> without authentication
1. get 
![get_non_authenticated](img/get%20all.png)
2. get details
![details_no_auth](img/details_no_auth.png)
3. post 
![post_no_auth](img/post_no_auth.png)
4. update
![update_no_auth](img/update_no_auth.png)
5. delete 
![delete_no_auth](img/delete_no_auth.png)

> token 
1. get token for user 
![token](img/token.png)
2. get refresh token
![refresh token](img/refresh_token.png)

> With authentication

1. update
![update](img/update_with_auth.png)
2. delete
![delete](img/delete_with_auth.png)