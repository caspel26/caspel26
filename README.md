<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:1e1b4b,50:6d28d9,100:c4b5fd&height=220&section=header&text=Hi%2C%20I'm%20Giuseppe%20%F0%9F%91%8B&fontSize=42&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Software%20Engineer%20%40%20Namirial%20Group&descAlignY=55&descSize=18" width="100%"/>

<img src="assets/terminal.gif" alt="Terminal session: whoami, cat about.txt, ls projects/" width="100%" />

<a href="https://caspel26.github.io"><img src="https://img.shields.io/badge/caspel26.github.io-portfolio-1E1B4B?style=for-the-badge&labelColor=6D28D9" alt="Portfolio" /></a>

</div>

<!-- ============ ABOUT ============ -->
### About Me

I write backend software for a living — cybersecurity and PKI with the Namirial Group — and frameworks, developer tools and small products for fun. Mostly Python and Go, almost always around APIs. I work AI-first: prompt engineering and agentic programming are part of how I design, build and test.

```python
caspel26 = {
    "work":      "cybersecurity · PKI @ Namirial Group",
    "languages": ["Python", "Go", "TypeScript"],
    "likes":     ["backend", "APIs", "developer tools"],
    "practice":  "AI-first · agentic programming",
    "editor":    "Lilac Nights, obviously",
    "portfolio": "https://caspel26.github.io",
}
```

Outside the day job, I maintain **[django-ninja-aio-crud](https://github.com/caspel26/django-ninja-aio-crud)**, an async CRUD framework for Django Ninja with 50+ stars, and **[goninja](https://github.com/caspel26/goninja)**, its Go counterpart — same idea, opposite approach: it generates the CRUD as real Go source instead of resolving it at runtime. I'm also building **[shimwire](https://github.com/caspel26/shimwire)**, a Bun/TypeScript CLI that mocks and tests APIs from the same OpenAPI spec.

<!-- ============ FEATURED PROJECTS ============ -->
### Featured Projects

#### [django-ninja-aio-crud](https://github.com/caspel26/django-ninja-aio-crud)

Async dynamic CRUD framework for Django Ninja.

- ⚡ Async-first API generation
- 🔐 Built-in authentication
- 🔎 Filtering & pagination
- 🧩 Dynamic model CRUD
- 📦 Automatic serialization
- 🤖 MCP server for AI agents — expose ViewSets as tools any MCP client can call directly, zero glue code
- 🐍 Django + Django Ninja

[Documentation](https://django-ninja-aio.com) · [PyPI](https://pypi.org/project/django-ninja-aio-crud/) · [GitHub](https://github.com/caspel26/django-ninja-aio-crud)

```
pip install django-ninja-aio-crud
```

<img src="https://img.shields.io/pypi/v/django-ninja-aio-crud?style=flat-square&label=pypi&labelColor=1E1B4B&color=6D28D9" /> <img src="https://img.shields.io/pypi/pyversions/django-ninja-aio-crud?style=flat-square&label=python&labelColor=1E1B4B&color=4C1D95" /> <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/caspel26/caspel26/main/badges/downloads.json&style=flat-square" /> <img src="https://img.shields.io/github/stars/caspel26/django-ninja-aio-crud?style=flat-square&label=stars&labelColor=1E1B4B&color=6D28D9" />

<img src="https://raw.githubusercontent.com/caspel26/django-ninja-aio-crud/main/docs/images/quickstart-demo.gif" alt="django-ninja-aio-crud quick start demo" width="100%" />

<br>

#### [goninja](https://github.com/caspel26/goninja)

Code-first CRUD REST APIs for Go, generated from annotated structs.

- 🧬 Annotate a struct, run one command, get real `.go` files you commit
- 🚫 Zero reflection on the request path — a bad tag fails `go build`, not production
- 🧷 Output types are separate structs, so a field can't leak into a response
- 🪢 No N+1 by construction — `list` never preloads, `retrieve` preloads what it carries
- 🔎 Filters, range queries, ordering and limit/offset pagination
- 🔐 `Authenticator` objects, per-route policy, reflected into the OpenAPI security schemes
- 📘 OpenAPI 3.0 with Swagger UI and ReDoc embedded — no external CDN
- 🐹 Plain `net/http` + GORM, no custom router

[Documentation](https://goninja.dev) · [Changelog](https://goninja.dev/docs/changelog/) · [GitHub](https://github.com/caspel26/goninja)

```
go install github.com/caspel26/goninja/cmd/goninja@latest
```

<img src="https://img.shields.io/github/v/release/caspel26/goninja?style=flat-square&label=release&labelColor=1E1B4B&color=6D28D9" /> <img src="https://img.shields.io/badge/go-1.25%2B-1E1B4B?style=flat-square&logo=go&logoColor=A78BFA" /> <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/caspel26/goninja/main/coverage-badge.json&style=flat-square" /> <img src="https://img.shields.io/github/license/caspel26/goninja?style=flat-square&labelColor=1E1B4B&color=A78BFA" /> <img src="https://img.shields.io/github/stars/caspel26/goninja?style=flat-square&label=stars&labelColor=1E1B4B&color=6D28D9" />

<img src="https://raw.githubusercontent.com/caspel26/goninja/main/docs/demo/vscode-demo.gif" alt="goninja quick start demo" width="100%" />

<br>

#### [shimwire](https://github.com/caspel26/shimwire)

One CLI for both sides of an API you don't fully control yet — mocks the parts that aren't built, and tests the parts that are, from a single OpenAPI/Swagger spec.

- 🔀 Spec-driven mock server and test collections, from one shared engine
- 📁 Git-native collections — plain TOML, reviewable in a normal PR diff
- 🎭 Schema-aware fake data, not just random junk
- 🎯 Overrides for status/latency/exact-body edge-case testing
- 🖱️ Guided interactive menu, or full CI-friendly flags
- 📊 HTML reports and `--fail-on-error` for CI
- 🤖 MCP server — an AI agent can inspect a spec, scaffold a project, and verify it actually works, without knowing shimwire's flags

[GitHub](https://github.com/caspel26/shimwire)

```
npm install -g shimwire
```

<img src="https://img.shields.io/npm/v/shimwire?style=flat-square&label=npm&labelColor=1E1B4B&color=6D28D9" /> <img src="https://github.com/caspel26/shimwire/actions/workflows/ci.yml/badge.svg" /> <img src="https://img.shields.io/badge/runtime-bun-1E1B4B?style=flat-square&logo=bun&logoColor=white" /> <img src="https://img.shields.io/badge/lang-TypeScript-6D28D9?style=flat-square&logo=typescript&logoColor=white" /> <img src="https://img.shields.io/github/license/caspel26/shimwire?style=flat-square&labelColor=1E1B4B&color=A78BFA" /> <img src="https://img.shields.io/github/stars/caspel26/shimwire?style=flat-square&label=stars&labelColor=1E1B4B&color=6D28D9" />

<img src="https://raw.githubusercontent.com/caspel26/shimwire/main/assets/terminal-demo.gif" alt="shimwire terminal demo" width="100%" />

<br>

#### [lilac-nights](https://github.com/caspel26/lilac-nights)

A dark VS Code theme with a lilac spine — built to be read for eight hours straight.

- 🟣 Purple carries the structure — keywords, properties, decorators
- 🎨 Every other hue has exactly one job, so nothing looks alike by accident
- 🔍 Semantic-token aware, down to `variable.classMember` for Python attributes
- ♿ Every syntax color clears WCAG AA against the editor background
- 🖥️ Full workbench, terminal ANSI, diff, debug and notebook coverage

[Open VSX](https://open-vsx.org/extension/caspel26/lilac-nights) · [GitHub](https://github.com/caspel26/lilac-nights)

```
codium --install-extension caspel26.lilac-nights
```

<img src="https://img.shields.io/open-vsx/v/caspel26/lilac-nights?style=flat-square&label=open%20vsx&labelColor=1E1B4B&color=6D28D9" /> <img src="https://img.shields.io/open-vsx/dt/caspel26/lilac-nights?style=flat-square&label=downloads&labelColor=1E1B4B&color=A78BFA" /> <img src="https://img.shields.io/badge/theme-dark-1E1B4B?style=flat-square" /> <img src="https://img.shields.io/github/license/caspel26/lilac-nights?style=flat-square&labelColor=1E1B4B&color=A78BFA" /> <img src="https://img.shields.io/github/stars/caspel26/lilac-nights?style=flat-square&label=stars&labelColor=1E1B4B&color=6D28D9" />

Previews — click a language to open it here:

<details>
<summary><img src="https://img.shields.io/badge/Python-1E1B4B?style=flat-square&logo=python&logoColor=A78BFA" alt="Python" /></summary>
<br>
<img src="https://raw.githubusercontent.com/caspel26/lilac-nights/main/images/preview-python.png" alt="Lilac Nights in Python" width="100%" />
</details>

<details>
<summary><img src="https://img.shields.io/badge/TypeScript-1E1B4B?style=flat-square&logo=typescript&logoColor=A78BFA" alt="TypeScript" /></summary>
<br>
<img src="https://raw.githubusercontent.com/caspel26/lilac-nights/main/images/preview-typescript.png" alt="Lilac Nights in TypeScript" width="100%" />
</details>

<details>
<summary><img src="https://img.shields.io/badge/JavaScript-1E1B4B?style=flat-square&logo=javascript&logoColor=A78BFA" alt="JavaScript" /></summary>
<br>
<img src="https://raw.githubusercontent.com/caspel26/lilac-nights/main/images/preview-javascript.png" alt="Lilac Nights in JavaScript" width="100%" />
</details>

<details>
<summary><img src="https://img.shields.io/badge/Go-1E1B4B?style=flat-square&logo=go&logoColor=A78BFA" alt="Go" /></summary>
<br>
<img src="https://raw.githubusercontent.com/caspel26/lilac-nights/main/images/preview-go.png" alt="Lilac Nights in Go" width="100%" />
</details>

<details>
<summary><img src="https://img.shields.io/badge/Rust-1E1B4B?style=flat-square&logo=rust&logoColor=A78BFA" alt="Rust" /></summary>
<br>
<img src="https://raw.githubusercontent.com/caspel26/lilac-nights/main/images/preview-rust.png" alt="Lilac Nights in Rust" width="100%" />
</details>

<details>
<summary><img src="https://img.shields.io/badge/C%2B%2B-1E1B4B?style=flat-square&logo=cplusplus&logoColor=A78BFA" alt="C++" /></summary>
<br>
<img src="https://raw.githubusercontent.com/caspel26/lilac-nights/main/images/preview-cpp.png" alt="Lilac Nights in C++" width="100%" />
</details>

<!-- ============ CURRENTLY ============ -->
### Currently

- Building async CRUD/backend infrastructure in Python and Go
- Integrating LLMs into production backends — tool calling, agentic workflows, structured outputs, RAG, async/streaming inference
- Exploring system design and architecture patterns for async services

<!-- ============ STACK ============ -->
### Stack

<p>
<img src="https://skillicons.dev/icons?i=python,go,ts,js&theme=dark" alt="Python, Go, TypeScript, JavaScript" /><br>
<sub><b>Languages</b></sub>
</p>

<p>
<img src="https://skillicons.dev/icons?i=django,fastapi,nodejs,bun&theme=dark" alt="Django, FastAPI, Node.js, Bun" /><br>
<sub><b>Backend</b> · also Django Ninja, Gin, Echo, Huma, GORM</sub>
</p>

<p>
<img src="https://skillicons.dev/icons?i=vue,nextjs,tailwind&theme=dark" alt="Vue, Next.js, Tailwind CSS" /><br>
<sub><b>Frontend</b> · also Framer Motion · used in my projects, with AI assistance for the implementation</sub>
</p>

<p>
<img src="https://skillicons.dev/icons?i=postgres,mysql,sqlite,redis&theme=dark" alt="PostgreSQL, MySQL, SQLite, Redis" /><br>
<sub><b>Data</b></sub>
</p>

<p>
<img src="https://skillicons.dev/icons?i=docker,linux,nginx,git,github,githubactions,gitlab,jenkins,cloudflare,aws&theme=dark" alt="Docker, Linux, Nginx, Git, GitHub, GitHub Actions, GitLab, Jenkins, Cloudflare, AWS" /><br>
<sub><b>DevOps</b> · also HAProxy, Oracle Cloud</sub>
</p>

<p><sub><b>Testing</b> · Pytest · Playwright</sub><br>
<sub><b>AI · LLM</b> · Anthropic · OpenAI · Gemini · Perplexity</sub></p>

<!-- ============ OTHER PROJECTS ============ -->
### Other Projects

- **[Shiori](https://myshiori.eu)** — an anime discovery and tracking product, in public beta (Go, PostgreSQL)
- **[mana-oly-tools](https://mana-oly-tools.pages.dev/)** — community calculators, planners and trackers for Olympus Prison on ManaCube
- **[ninja-aio-blog-example](https://github.com/caspel26/ninja-aio-blog-example)** — production-oriented example integrating django-ninja-aio-crud with JWT (RS256) authentication

#### Other Experiments

- **[ssh-manager](https://github.com/caspel26/ssh-manager)** — a Vue-based SSH connection manager
- **[password_manager](https://github.com/caspel26/password_manager)** — a desktop password manager (Electron, Vue 3, TypeScript) that keeps credentials in encrypted local vault files

<!-- ============ CONNECT ============ -->
### Connect

<a href="https://caspel26.github.io"><img src="https://img.shields.io/badge/Portfolio-6D28D9?style=flat-square&logo=githubpages&logoColor=white" /></a> <a href="https://www.linkedin.com/in/giuseppe-casillo-3737b128b/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" /></a> <a href="mailto:peppe.c0126@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=flat-square&logo=gmail&logoColor=white" /></a> <a href="https://github.com/caspel26"><img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white" /></a>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:c4b5fd,50:6d28d9,100:1e1b4b&height=100&section=footer" width="100%"/>
