#!/usr/bin/env bash
# ============================================================
# Cevano IT Solutions — push local secrets to Cloudflare Pages
# ============================================================
# This is the closest equivalent to "importing a .env file" that
# Cloudflare actually supports: it reads your local .dev.vars and pushes
# the SECRET values to your live Cloudflare Pages project using the
# official `wrangler` CLI — so you don't have to copy/paste them into the
# dashboard by hand.
#
# Plain (non-secret) variables — TO_EMAIL, FROM_EMAIL — are NOT pushed by
# this script. They aren't sensitive, so it's just as easy (and clearer)
# to type those two directly into Cloudflare Pages → Settings →
# Environment variables yourself.
#
# USAGE:
#   1. Make sure you've created a real .dev.vars file (see .dev.vars.example)
#      with your actual Resend API key filled in.
#   2. Install wrangler if you don't have it:  npm install -g wrangler
#   3. Log in once:                            npx wrangler login
#   4. Run this script:                        bash scripts/push-secrets-to-cloudflare.sh <project-name>
#
# <project-name> is the name you gave the project in Cloudflare Pages
# (visible in the dashboard URL / project settings).

set -euo pipefail

PROJECT_NAME="${1:-}"
DEV_VARS_FILE="$(dirname "$0")/../.dev.vars"

if [ -z "$PROJECT_NAME" ]; then
  echo "Usage: bash scripts/push-secrets-to-cloudflare.sh <cloudflare-pages-project-name>"
  exit 1
fi

if [ ! -f "$DEV_VARS_FILE" ]; then
  echo "No .dev.vars file found at $DEV_VARS_FILE"
  echo "Copy .dev.vars.example to .dev.vars and fill in your real values first."
  exit 1
fi

get_value () {
  # Reads KEY=value from .dev.vars, ignoring blank/comment lines.
  grep -E "^$1=" "$DEV_VARS_FILE" | head -n1 | cut -d'=' -f2- || true
}

RESEND_API_KEY_VALUE="$(get_value RESEND_API_KEY)"
TURNSTILE_SECRET_KEY_VALUE="$(get_value TURNSTILE_SECRET_KEY)"

if [ -z "$RESEND_API_KEY_VALUE" ] || [ "$RESEND_API_KEY_VALUE" = "re_your_real_resend_api_key_here" ]; then
  echo "RESEND_API_KEY is missing or still set to the placeholder in .dev.vars — fill in your real key first."
  exit 1
fi

echo "Pushing RESEND_API_KEY to Cloudflare Pages project '$PROJECT_NAME' (production)..."
echo "$RESEND_API_KEY_VALUE" | npx wrangler pages secret put RESEND_API_KEY --project-name "$PROJECT_NAME"

if [ -n "$TURNSTILE_SECRET_KEY_VALUE" ]; then
  echo "Pushing TURNSTILE_SECRET_KEY to Cloudflare Pages project '$PROJECT_NAME' (production)..."
  echo "$TURNSTILE_SECRET_KEY_VALUE" | npx wrangler pages secret put TURNSTILE_SECRET_KEY --project-name "$PROJECT_NAME"
else
  echo "TURNSTILE_SECRET_KEY is empty in .dev.vars — skipped (fine if you're not using Turnstile yet)."
fi

echo ""
echo "Done. Now set the two plain (non-secret) variables manually in the"
echo "Cloudflare dashboard — Pages → $PROJECT_NAME → Settings → Environment"
echo "variables:"
echo "  TO_EMAIL   = enquiries@cevano.co.uk"
echo "  FROM_EMAIL = Cevano Website <onboarding@resend.dev>   (or your verified sending address)"
echo ""
echo "Then redeploy (or push a new commit) for the Function to pick up the changes."
