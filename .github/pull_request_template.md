## Summary

## Verification

- [ ] Catalog validation and compatibility tests pass.
- [ ] `catalog.json` matches manifests (regenerate deliberately, review the diff).

## Runtime dependency (if applicable)

- Parent issue / delivery owner:
- Companion `openlia/openlia` PR:
- Actual first compatible runtime release / `requires.openlia`:
- Combined runtime/templates integration run and exact SHAs:
- Rollout: deploy runtime first, update/rebase templates, verify the deployment.

Run the **Runtime and templates integration** workflow in `openlia/openlia` with
the proposed runtime and templates refs. Link the same run from both PRs.
Browser acceptance must use the actual catalog composition, not a copied fixture.
