
.PHONY: cleanup
cleanup:
	uv tool run pre-commit install
	uv tool run pre-commit run --all
