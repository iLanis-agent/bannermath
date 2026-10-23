# Banner Math

Event banner roll, week, cost and time arithmetic. The 260 banners at 12 banners a roll take 22 rolls, the last roll holding 8 banners.

## Named constants

None. Every number is the owner's own entry.

## What it computes

- **The rolls truth** - the banners (1 to 1000000) divided by the banners a roll (1 to 1000), rounded up, with what the last roll holds.
- **The weeks truth** - the banners divided by the banners used a week (1 to 100000), with the banners left for the next week.
- **The cost truth** - the rolls (1 to 100000) times the roll price ($0.01 to $999.99) to the cent, and spread over the banners, half rounded up.
- **The time truth** - the banners divided by the banners printed a minute (1 to 100), rounded up, in minutes and in hours and minutes.

## Boundary

Arithmetic only. Counting applied as written. It has not seen any banner, roll or press and does not know whether banners will really arrive unfaded, a press will jam or a price will hold, and it gives no verdict that a roll is worth its price or a banner is right for an event. Every number is the owner's own entry.

## Files

- `index.html` - landing page with the boundary and starting examples.
- `app.html` - the calculator; every box recomputes on each keystroke.
- `engine.js` - the four truths, shared by the page and the tests.
- `oracle.py` - an independent Python re-implementation; writes `expected.json`.
- `test.js` - runs the engine against `expected.json` (99 cases, 20 error cases).

## Tests

```
python3 oracle.py
node test.js
```
