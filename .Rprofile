.First <- function() {
 options(
  repos = c(CRAN = 'https://cran.rstudio.com',
            USGS = 'https://owi.usgs.gov/R'),
  help_type = 'text',
  width = 80,
  github.user = 'jsta',
  devtools.name = 'Joseph Stachelek',
  devtools.desc = list(
      `Authors@R` = paste0("person(\"Joseph\", \"Stachelek\", ",
	"comment = c(ORCID = \"0000-0002-5924-2464\", ",
	"role = c(\"aut\", \"cre\"), \n email = \"stachel2@msu.edu\")"),
       License = 'GPL',
       Version = '0.1'),
  warnPartialMatchAttr = TRUE,
  warnPartialMatchDollar = TRUE
)
}

if (interactive()) {
  suppressMessages(require(devtools))
  suppressMessages(require(remedy))
  suppressMessages(require(datapasta))
}

options(error = NULL,
        usethis.description = list(
          `Authors@R` = 'person("Joseph", "Stachelek", email = "stachel2@msu.edu", role = c("aut", "cre"))',
          License = "MIT + file LICENSE"
        )
)

Sys.setenv(NOT_CRAN = "true")
Sys.setenv("_R_S3_METHOD_REGISTRATION_NOTE_OVERWRITES_" = 0)
