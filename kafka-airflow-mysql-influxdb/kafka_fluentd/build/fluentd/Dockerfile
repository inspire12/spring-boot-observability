FROM fluent/fluentd:edge-debian

USER root

RUN apt update && apt upgrade
RUN apt install -y curl
RUN fluent-gem install fluent-plugin-kafka
RUN fluent-gem install fluent-plugin-rewrite-tag-filter fluent-plugin-multi-format-parser
RUN fluent-gem install fluent-plugin-s3
USER fluent
ENTRYPOINT ["tini",  "--", "/bin/entrypoint.sh"]
CMD ["fluentd"]