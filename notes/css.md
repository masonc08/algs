# CSS

- Source: https://www.youtube.com/watch?v=1PnVor36_40
- CSS is a styling language used to style and express HTML content

## Selectors

- CSS is made of selectors, which can be used to describe HTML elements, classes, and ids
- any HTML element can be used with a selector, such as `h1`, `strong`, etc
- class selectors are the most useful selector, as you can select html elements based on their class attribute
    - very useful as they are great for creating reusable components
- use `.className` to select a CSS class name
- use `class="btn btn-1"` to use `btn-1` selector, which extends off `btn` selector
- can element can only have one ID, but can have multiple selectors
- use `#id` for selector on an ID
    - usually not required
- target multiple classes with one selector by using `.class1.class2.classn`
- select tags by an ancestor-child relationship by using `ancestor child` tag
    - eg. `div p` to select all `<p>` tags with `<div>` as their parent
- to have a selector apply to multiple other selectors, use a comma to separate them
    - `.selector1, .selector2` to override and extend `selector` and `selector2` independently
- `*` selector selects the target for all styles on the webpage
- CSS can be written inline directly on the HTML with the `style` tag, or using the `<style>` tag inside the html, or have a separate CSS file and link to it within the HTML using the `<link>` tag, with `rel="stylesheet"` attribute
- id selectors always takes precedence over class selectors, which take precedence over element selectors
- most html tags will have inherited CSS elements, like `h1` always having margins

## Colours

- hex codes are broken into 3 sets of 2-digit hexadecimal numbers, where each 2-digit hexadecimal number represents R, G, B respectively
- `rgba` for transparency options, where `a=1` means fully opaque, `a=0` is fully transparent
    - or 4 sets of 2-digit hexadecimal numbers, with the last hexadecimal set representing transparency
- `hsl` stands for hue, saturation, lightness
    - hue goes from 0 to 360, determines which number touse
    - saturation is from 0 to 100, determines how colourful the colour is
        - 0 saturation means there is no colour in it, somewhere on the greyscale
        - 100 means the colour is as bright as it can be
    - lightness determines how bright the colour is, 100 being a completely white colour, 0 being a completely black colour
    - also has `hsla`

## Box Model

- padding is spacing between content and border, margin is the space on the outside of the border, so elements can be spaced away from each other
- pixels are the primary unit, which are a fixed with no matter how big your screen is
- percentages are relative to the space of its parent container
- em is mostly used for fonts and font related situations, like padding and margins around fonts
    - em is relative to the font size, if font size is 16, 1em becomes 16 pixels, 2em is 32pixels, etc
- rem is similar to em, but scales off the root font size

## Positioning

- static positioning is the default, and displays as expected in the HTML structure
- absolute positioning allows document to ignore the item, removing it from the document flow
- good for wanting something to stick to a specific position, but nothing else around it to move
    - can move item absolutely to another position, relative to another relative parent
- fixed positioning are fixed to the entire HTML element, ignores any relative parents
    - it also sticks to the page as the user scrolls
- sticky position is a combination of relative and fixed positioning, where the element is relative by default but becomes fixed once it is scrolled out of the page

## Flexbox

- use `display: flex;` to initalize a flexbox container, where the container can control the positioning and display of its children
- flexbox items align themselves on the main axis
- `justify-content` to style relative to main axis
    - `flex-start` for start of main axis, `center` for center of main axis
- children are stretched to cross axis by default
- `flex-wrap: wrap` allows children to not shrink when the main container is compressed, the children instead stack on each other on the cross axis
- flexbox container should be responsible for styling and positioning flex children, flexbox children should be responsible for overriding flex rules
- `flex-shrink` to customize shrinking for a certain flex child
- `flex-grow` to customize growing for a certain flex child
- `align-self` on a flex child to override align-content from the parent container, on the cross axis
- `order` applied on flex children can change the order that flex children are arranged in, without having to touch any HTML
- shorthands for the above are `flex: grow shrink basis;`
