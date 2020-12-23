---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.12
    jupytext_version: 1.6.0
kernelspec:
  display_name: bayes_book
  language: python
  name: bayes_book
---

# Test for book

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt
```

```{code-cell} ipython3
x = np.random.randn(50)
y = np.random.randn(50)
```

```{code-cell} ipython3
---
render:
  figure:
    caption: "This is a test for a plot caption"
    name: fig:test-caption
---
plt.plot(x, y, "o");
```

```{code-cell} ipython3
plt.plot(y, x, "o");
```
