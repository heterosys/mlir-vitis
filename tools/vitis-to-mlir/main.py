#!/usr/bin/env python3

import click


@click.group(chain=True)
@click.option('--verbose',
              '-v',
              default=0,
              count=True,
              help='Increase logging verbosity.')
@click.option('--quiet',
              '-q',
              default=0,
              count=True,
              help='Decrease logging verbosity.')
@click.pass_context
def entry_point(ctx, verbose, quiet):
  # Setup execution context
  obj = ctx.ensure_object(dict)


if __name__ == '__main__':
  entry_point()
