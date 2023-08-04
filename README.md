
_DHQwords_ is a mashup of [DHQ](http://www.digitalhumanities.org/dhq/) (_Digital Humanities Quarterly_) and [_Startwords_](https://startwords.cdh.princeton.edu/).  

Articles from _DHQ_ have been converted from TEI XML to markdown for publication as Hugo site using the _Startwords_ theme.

_DHQ_ content is (generally) published under the [Creative Commons Attribution-NoDerivatives 4.0 International (CC BY-ND 4.0) license](https://creativecommons.org/licenses/by-nd/4.0/). Making that content available in a different format is expressly allowed by all CC licenses, including those with the No Derivatives clause. See the answer to [Can I take a CC-licensed work and use it in a different format?](https://creativecommons.org/faq/#can-i-take-a-cc-licensed-work-and-use-it-in-a-different-format) in the Creative Commons FAQ.

_Startwords_ is a research periodical irregularly published by the [Center for Digital Humanities at Princeton](https://cdh.princeton.edu). Read more [about _Startwords_ editorial and technical work](https://startwords.cdh.princeton.edu/about/).

---

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Hugo](https://img.shields.io/badge/hugo-0.116-blue.svg)](https://gohugo.io)
![Node version](https://img.shields.io/badge/node-18-blue)

## Developing

### Hugo setup

To run the site locally for development, first follow the [instructions to install
Hugo](https://gohugo.io/getting-started/installing/). You can check that Hugo
is installed with:

```sh
$ hugo version
```

this should output version info like:

```
Hugo Static Site Generator v0.116.0/extended darwin/amd64 BuildDate: unknown
```

check that the version you installed is at least as new as the version shown in
the hugo badge at the top of this file.

## importing DHQ content

(notes todo)


### Static files

After hugo is installed, you'll need to install the javascript dependencies that
are used to compile the site's static files. To check if you have node installed:

```sh
$ node --version
```

This should output a version string that is at least as new as the version shown
in the node badge at the top of this file. To install dependencies, run npm in
the project's root directory:

```sh
$ npm install
```

If the install completes without errors, you're ready to build the site for
development.

### Serving locally

To run a development server with auto-reload:

```sh
$ hugo server -D
```

You should see some debug output, followed by:

```sh
Web Server is available at http://localhost:1313/ (bind address 127.0.0.1)
Press Ctrl+C to stop
```

Open a web browser to the above address to see a local version of the site. When
you make changes and save files locally, hugo will automatically refresh the page.

## License

### Content
Content published in _DHQ_ is licensed under the Creative Commons Attribution 4.0 N-Derivatives International License (CC-BY-ND).

### Software

Software included in _Startwords_ is licensed under the [Apache 2.0 License](LICENSE).

