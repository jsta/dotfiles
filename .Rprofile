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

           # "_R_CHECK_LENGTH_1_CONDITION_" = "package:_R_CHECK_PACKAGE_NAME_,verbose")

#### See - https://github.com/csgillespie/rprofile
#' @title Choose RStudio project
#'
#' Command line version for choosing RStudio projects
#' @param path Default \code{NULL}. If not \code{NULL}, path is passed to \code{op}.
#' @examples
#' \dontrun{
#' cp()
#' }
#' @export
cp = function(path = NULL) {
  if (!is.null(path)) {
    op(path)
    return(invisible(NULL))
  }
  projs_paths = readLines("~/.rstudio-desktop/monitored/lists/project_mru") #nolint
  projs_paths = c(getwd(),
                  projs_paths[file.exists(projs_paths)][1:9])
  projs_paths = projs_paths[!is.na(projs_paths)]

  ## Get project name
  projs = gsub(basename(projs_paths), pattern = ".Rproj", replacement = "")
  projs[1] = "Current dir"
  projs = paste0(crayon::bold(seq_along(projs) - 1), ". ", crayon::cyan(projs))
  projs[1] = paste0(" ", projs[1])

  ## Get project directory
  projs_dir = dirname(projs_paths)
  tilde = path.expand("~")
  projs_dir = stringr::str_replace(projs_dir, tilde, "~")

  path_split = stringr::str_split(projs_dir, pattern = "/")
  path_lens = unlist(lapply(path_split, length))
  path_start = path_lens - 2
  path_start = pmax(path_start, 0)

  shorten_path = purrr::imap_chr(path_split,
                                 ~ paste(.x[path_start[.y]:path_lens[.y]],
                                         collapse = .Platform$file.sep))

  all = paste0(projs, " (", crayon::italic(shorten_path), ")\n")
  cat(all)

  proj_number = readline("Select Project: ")
  proj_number = as.numeric(proj_number)


  if (is.na(proj_number) || proj_number == 0) op()
  else op(projs_paths[proj_number + 1])
}

ip = function(path = getwd()) {
  rstudioapi::initializeProject(path)
  op(path)
}

#' @title RStudio projects
#'
#' A command line version of opening RStudio projects.
#' @param path Path to the (proposed) RStudio project.
#' @examples
#' \dontrun{
#' # Open project in current working directory
#' op()
#' # Open project in current working directory
#' op("/path/to/project")
#' }
#' @export
op = function(path = ".") {
  path = normalizePath(path)
  proj = list.files(path, pattern = "\\.Rproj$")
  if (grepl("\\.Rproj$", path)) {
    setwd(dirname(path))
    rstudioapi::openProject(path)
  } else if (length(proj) == 0L) {
    message("No available project.")
    create_project = readline(prompt = "Create (y/N): ")
    if (tolower(create_project) == "y") {
      ip(path)
    }
  } else {
    setwd(path)
    rstudioapi::openProject(proj)
  }
}

####
