name: Feature request
about: Suggest a new feature, enhancement to **squiral**, etc.
body:
  - type: markdown
    attributes:
      value: |
         This is for issues for `squiral`.
  - type: input
    id: search
    attributes:
      label: Search you tried in the issue tracker
      placeholder: ...
    validations:
      required: true
  - type: markdown
    attributes:
      value: |
        95% of issues created are duplicates.
        Please try extra hard to find them first.
  - type: textarea
    id: freeform
    attributes:
      label: Describe the feature you'd like
      placeholder: 'I want to do ... This kind of feature would be useful because ...'
    validations:
      required: true
  - type: input
    id: version
    attributes:
      label: **squiral** version
      placeholder: pip list | grep squiral
    validations:
      required: true
