package com.linkedin.metadata.config;

import lombok.Data;


@Data
public class BuildIndicesConfiguration {

  private boolean cloneIndices;
  private boolean allowDocCountMismatch;
  private String retentionUnit;
  private Long retentionValue;
}
