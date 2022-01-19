library(tidyverse)
Oxides <- read_csv("C:/Users/ayersj.VANDERBILT/OneDrive - Vanderbilt/Papers/SpheneSolubility/DataAnalysis/FluorescenceTestV2.csv")
OxidesLong <- Oxides %>%
  pivot_longer(c("SiO2":"TiO2"), names_to = "Oxide", values_to = "Value")
p <- ggplot(OxidesLong, aes(x = x, y = Value)) +
  geom_point() +
  geom_smooth() +
  facet_wrap(facets = vars(Oxide), scales = "free_y", nrow = 3) +
  xlab("Distance from titanite crystal (μm)") +
  ylab("Oxide concentration (wt. %)") +
  theme_bw()
  # geom_point(aes(y=SiO2)) +
  # geom_smooth(aes(y=SiO2)) +
  # geom_point(aes(y=TiO2)) +
  #geom_smooth(aes(y=TiO2), color = "brown") +
  # See https://www.r-graph-gallery.com/line-chart-dual-Y-axis-ggplot2.html  
# scale_y_continuous(
#     name = "SiO2",
#     sec.axis = sec_axis(~./100, name = "TiO2")
#   ) +
#   theme(
#     axis.title.y = element_text(size = 13),
#     axis.title.y.right = element_text(size = 13)
#   )
# TiO2 does not seem to plot second axis. Use facet_wrap instead.
print(p)
ggsave("FluorescenceTest.eps", width = 2000, height = 2*618, units = "px", plot = p)