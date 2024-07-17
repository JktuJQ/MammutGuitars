# MAMMUT Guitars

**MAMMUT Guitars** is an online multipage guitar blog/shop.

Making and playing guitars is one of my hobbies that I excel at,
and making a website that shows my works would be a great learning project.


### Sections and routing
* Main page ('/' route)
* Page with all guitars ('/guitars' route)
* Page with single guitar ('/guitars/<id>' route)
* 'About me' section ('/about' route)

All pages have the same navigation bar (with the difference of highlighted section) and footer.
Those provide useful links (for other pages on website or to my socials).


### Main page

Main page has short description of me, embedded videos from YouTube and info for my favorite guitars.

Here how it looks like:
![Main page](/screenshots/index.png)

Links are highlighted with orange color when you hover cursor over them.


### 'All guitars' page

This page just lists all my guitars (both past and present). There are 23 of them.
The only difference of guitars display from main page is that there is also info about their history.

Since there are too many of those guitars 
(you can see their images in 'frontend/static/assets/guitars/' folder),
following screenshot does not cover the whole page:
![All guitars](/screenshots/guitars.png)


### 'Single guitar' page

Here how 'single guitar' page looks like:
![Guitar](/screenshots/guitar.png)


### 'About me' page

'About me' page contains a bit more info about me.

Here how it looks like:
![About me](/screenshots/about.png)


### Summary

This multipage website is a great project
to learn basics of fullstack development (backend, frontend and database setup).
Unfortunately, it won't be hosted on any domain,
so the only way to actually view the website is to try to start it yourself!
All you need is to use Python to run `main.py` script, and then go to `http://127.0.0.1:8080/`,
where you will be able to see it.

Feel free to use this project to improve your skills of fullstack development!
