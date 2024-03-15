#let project(title: "", authors: (),student_number: (), class: (), date: none, body) = {
  // Set the document's basic properties.
  set document(author: authors, title: title)
  set page(numbering: "1", number-align: center)
  set text(font: "Linux Libertine")
  // Title row.

  // Author information.
  pad(
    top: 0.5em,
    bottom: 0.5em,
    x: 2em,
    grid(
      columns: (1fr,) * calc.min(4, authors.len()),
      gutter: 1em,
      ..authors.map(author => align(top+left)[Name: #strong(author)]),
      ..student_number.map(number => align(top+left)[Number: #strong(number)]),
      ..class.map(class => align(top+left)[Class: #strong(class)]),
    ),
  )
  align(center)[
    #block(text(weight: 700, 1.75em, title))
    #v(1em, weak: true)
    #date
  ]

  // Main body.
  set par(justify: true)

  body
}