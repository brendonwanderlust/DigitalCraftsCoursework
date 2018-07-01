<!DOCTYPE html>
<html>
  <head>
    <title>Flexbox - April 2017 - Fullstack</title>
    <meta charset="utf-8">
    <link rel="shortcut icon" href="/static/favicon.ico">
    <base target="_blank">
    <link rel="stylesheet" href="/static/css/slides.css">
  </head>
  <body>
    <textarea id="source">
class: inverse, spaced
layout: true
background-image: url(/static/img/dclogo.png)

---


class: center, middle

# Flexbox

---

# Historical Layout Systems

- [Python Tkinter Layouts](http://www.python-course.eu/tkinter_layout_management.php)
- pack -> flexbox
- grid -> new CSS spec
    - not to be confused with Grid Systems
- place -> absolute

---

# Why use flexbox

<iframe src="//giphy.com/embed/Rl9Yqavfj2Ula" width="240" height="180" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>

- ease of use, simplied HTML
- vertical centering is possible
- can have real colums that stay the same height and are responsive

---
# Flexbox Usage

- [Flexbox Playground](http://flexboxplayground.catchmyfame.com/)
- `display: flex` or `display: flex-inline`
- `flex-direction`: `row`, `column`
- `flex-wrap`: `wrap`, `no-wrap`
- `justify-content`: `flex-start`, `center`, `flex-end`, `space-between`, `space-around`
- `align-items`: `stretch`, `flex-start`, `center`, `flex-end`, `baseline`
- `align-content`: `flex-start`, `center`, `flex-end`, `space-between`, `space-around`


</textarea>
    <script src="https://remarkjs.com/downloads/remark-latest.min.js"></script>
    <script>
      var slideshow = remark.create({
        highlightStyle: 'zenburn',
        highlightLanguage: 'text',
        highlightLines: true
      });
    </script>
  </body>
</html>