---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.12
    jupytext_version: 1.6.0
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Mastering Bayes

_By Alex Andorra and Oriol Abril Pla_

```{toctree}
chapter1/index
about/index
zbibliography
```

```{code-cell} ipython3
a = "This is some"
b = "Python code!"
print(f"{a} {b}")
```

```
print("This is not shown because this is text formatted as code, not a code cell")
```

And now some text with some fancy math even $\mathcal{N}(\mu, \sigma)$.

Here is how one would create a cell with code that intentionally errors out:

```{code-cell}
:tags: [raises-exception]

print(thisvariabledoesntexist)
```

More details in [MyST-NB docs](https://myst-nb.readthedocs.io/en/latest/use/execute.html#dealing-with-code-that-raises-errors)
